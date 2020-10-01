import os

target_dir = "./testdir"

def find_files(suffix, path):
  all_paths = sorted(traverse_path(suffix, path))
  return search_prefix(all_paths, ".c")

def traverse_path(suffix, path):
  arr = []
  if os.path.isfile(os.path.join(f"{suffix}/{path}")):
    return os.path.join(f"{suffix}/{path}")
  else:
    for element in os.listdir(suffix):
      if os.path.isdir(os.path.join(f"{suffix}/{element}")):
        arr.append(os.path.join(f"{suffix}/{element}"))
        paths = traverse_path(os.path.join(f"{suffix}/{element}"), element)
        arr.extend(paths)
      else:
        arr.append(os.path.join(f"{suffix}/{element}"))
    return arr

def search_prefix(names, string):
  return list(filter(lambda name: name.endswith(string), names))


print(find_files(target_dir, target_dir))
# ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']
print(find_files(None, target_dir))
# []
print(find_files(None, None))
# []