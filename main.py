import asyncio
import glob
import os
import time
import typing

import aiofiles

import create_dummy_data


async def cat_files_in_async(directory_name, root_dir='.'):
    output_file_name = f'{directory_name}.txt'
    async with aiofiles.open(output_file_name, mode='w') as f:
        pass
    for file_path in glob.glob(root_dir + '/' + directory_name + '/*.txt'):
        async with aiofiles.open(file_path, mode='r') as f:
            file_content = await f.read()
        async with aiofiles.open(output_file_name, mode='a') as f:
            await f.write(str(file_path) + '\n' + str(file_content) + '\n\n')


async def cat_subdirectories_async(root_dir='.'):
    directory_children = glob.glob(root_dir + '/' + '*')
    subdirectory_names = filter(lambda f: os.path.isdir(f), directory_children)
    subdirectories = [subdirectory_name for subdirectory_name in subdirectory_names]
    for directory_name in subdirectories:
        await cat_files_in_async(directory_name, root_dir)


if __name__ == '__main__':
    # create_dummy_data()
    start = time.process_time()
    asyncio.run(cat_subdirectories_async())
    print(time.process_time() - start)