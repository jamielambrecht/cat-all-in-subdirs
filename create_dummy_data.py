from pathlib import Path

for i in range(12):
    subdir = Path(f'./{i}')
    if not subdir.exists():
        os.mkdir(subdir)
    file_names = [f'{char}.txt' for char in "ABCDEFG"]
    for file_name in file_names:
        file_path = Path(subdir, file_name)
        with open(file_path, 'w') as f:
            f.write(f'{file_name}\n') 