laptop={'merek': 'Axioo', 'CPU': 'I9 14H', 'ram_gb': '16', 'GPU':'RTX5080'}
print('data laptop:',laptop)
print('CPU:',laptop['CPU'])
laptop['storage_gb'] = 2048
laptop['ram_gb'] = '64'
print('Laptop Pongo Terbaru:', laptop)