import os
import json
import hashlib
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'

# Data storage paths
DATA_DIR = 'data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
CLASSES_FILE = os.path.join(DATA_DIR, 'classes.json')
ATTENDANCE_FILE = os.path.join(DATA_DIR, 'attendance.json')

# Initialize data directory
os.makedirs(DATA_DIR, exist_ok=True)

# Helper functions
def load_json(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

def save_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def init_data():
    """Initialize with default admin and guru accounts"""
    users = load_json(USERS_FILE)
    if not users:
        users = {
            'admin': {
                'password': hash_password('admin123'),
                'role': 'admin',
                'name': 'Administrator'
            },
            'guru1': {
                'password': hash_password('guru123'),
                'role': 'guru',
                'name': 'Guru Contoh'
            }
        }
        save_json(USERS_FILE, users)
    
    if not os.path.exists(CLASSES_FILE):
        save_json(CLASSES_FILE, {})
    
    if not os.path.exists(ATTENDANCE_FILE):
        save_json(ATTENDANCE_FILE, {})

init_data()

# Context processor
@app.context_processor
def inject_now():
    return {'now': datetime.now()}

# Routes
@app.route('/')
def index():
    if 'username' in session:
        if session['role'] == 'admin':
            return redirect(url_for('admin_dashboard'))
        else:
            return redirect(url_for('guru_dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        users = load_json(USERS_FILE)
        
        if username in users and users[username]['password'] == hash_password(password):
            session['username'] = username
            session['role'] = users[username]['role']
            session['name'] = users[username]['name']
            
            if users[username]['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('guru_dashboard'))
        else:
            flash('Username atau password salah!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'username' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    classes = load_json(CLASSES_FILE)
    users = load_json(USERS_FILE)
    
    # Count gurus
    guru_count = sum(1 for u in users.values() if u['role'] == 'guru')
    
    return render_template('admin_dashboard.html', 
                         classes=classes, 
                         class_count=len(classes),
                         guru_count=guru_count)

@app.route('/admin/manage_class', methods=['GET', 'POST'])
def manage_class():
    if 'username' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        action = request.form.get('action')
        classes = load_json(CLASSES_FILE)
        
        if action == 'add':
            class_name = request.form.get('class_name')
            students = request.form.get('students').split('\n')
            students = [s.strip() for s in students if s.strip()]
            
            class_id = datetime.now().strftime('%Y%m%d%H%M%S')
            classes[class_id] = {
                'name': class_name,
                'students': students,
                'created_at': datetime.now().isoformat()
            }
            save_json(CLASSES_FILE, classes)
            flash('Kelas berhasil ditambahkan!', 'success')
            
        elif action == 'delete':
            class_id = request.form.get('class_id')
            if class_id in classes:
                del classes[class_id]
                save_json(CLASSES_FILE, classes)
                flash('Kelas berhasil dihapus!', 'success')
        
        return redirect(url_for('manage_class'))
    
    classes = load_json(CLASSES_FILE)
    return render_template('manage_class.html', classes=classes)

@app.route('/admin/manage_user', methods=['GET', 'POST'])
def manage_user():
    if 'username' not in session or session['role'] != 'admin':
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        action = request.form.get('action')
        users = load_json(USERS_FILE)
        
        if action == 'add':
            username = request.form.get('username')
            password = request.form.get('password')
            name = request.form.get('name')
            role = request.form.get('role')
            
            if username in users:
                flash('Username sudah ada!', 'error')
            else:
                users[username] = {
                    'password': hash_password(password),
                    'role': role,
                    'name': name
                }
                save_json(USERS_FILE, users)
                flash('User berhasil ditambahkan!', 'success')
        
        elif action == 'delete':
            username = request.form.get('username')
            if username != 'admin' and username in users:
                del users[username]
                save_json(USERS_FILE, users)
                flash('User berhasil dihapus!', 'success')
        
        return redirect(url_for('manage_user'))
    
    users = load_json(USERS_FILE)
    return render_template('manage_user.html', users=users)

@app.route('/guru/dashboard')
def guru_dashboard():
    if 'username' not in session or session['role'] != 'guru':
        return redirect(url_for('login'))
    
    classes = load_json(CLASSES_FILE)
    attendance = load_json(ATTENDANCE_FILE)
    
    # Count today's attendance by this guru
    today = datetime.now().strftime('%Y-%m-%d')
    today_count = sum(1 for a in attendance.values() 
                     if a.get('date') == today and a.get('guru') == session['username'])
    
    return render_template('guru_dashboard.html', 
                         classes=classes,
                         class_count=len(classes),
                         today_attendance=today_count)

@app.route('/guru/attendance/<class_id>', methods=['GET', 'POST'])
def take_attendance(class_id):
    if 'username' not in session or session['role'] != 'guru':
        return redirect(url_for('login'))
    
    classes = load_json(CLASSES_FILE)
    
    if class_id not in classes:
        flash('Kelas tidak ditemukan!', 'error')
        return redirect(url_for('guru_dashboard'))
    
    if request.method == 'POST':
        attendance = load_json(ATTENDANCE_FILE)
        
        attendance_id = datetime.now().strftime('%Y%m%d%H%M%S')
        attendance_data = {
            'class_id': class_id,
            'class_name': classes[class_id]['name'],
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': datetime.now().strftime('%H:%M:%S'),
            'guru': session['username'],
            'guru_name': session['name'],
            'students': {}
        }
        
        for student in classes[class_id]['students']:
            status = request.form.get(f'status_{student}')
            attendance_data['students'][student] = status
        
        attendance[attendance_id] = attendance_data
        save_json(ATTENDANCE_FILE, attendance)
        
        flash('Absensi berhasil disimpan!', 'success')
        return redirect(url_for('guru_dashboard'))
    
    return render_template('take_attendance.html', 
                         class_data=classes[class_id],
                         class_id=class_id)

@app.route('/reports')
def reports():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    attendance = load_json(ATTENDANCE_FILE)
    classes = load_json(CLASSES_FILE)
    
    # Filter by role
    if session['role'] == 'guru':
        attendance = {k: v for k, v in attendance.items() 
                     if v.get('guru') == session['username']}
    
    return render_template('reports.html', 
                         attendance=attendance,
                         classes=classes)

@app.route('/reports/detail/<attendance_id>')
def report_detail(attendance_id):
    if 'username' not in session:
        return redirect(url_for('login'))
    
    attendance = load_json(ATTENDANCE_FILE)
    
    if attendance_id not in attendance:
        flash('Data absensi tidak ditemukan!', 'error')
        return redirect(url_for('reports'))
    
    data = attendance[attendance_id]
    
    # Check permission
    if session['role'] == 'guru' and data.get('guru') != session['username']:
        flash('Anda tidak memiliki akses ke data ini!', 'error')
        return redirect(url_for('reports'))
    
    return render_template('report_detail.html', 
                         attendance_id=attendance_id,
                         data=data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
