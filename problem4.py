class Group(object):
  def __init__(self, _name):
    self.name = _name
    self.groups = []
    self.users = []
  def add_group(self, group):
    self.groups.append(group)
  
  def add_user(self, user):
    self.users.append(user)
  
  def get_groups(self):
    return self.groups
  
  def get_users(self):
    return self.users
  
  def get_name(self):
    return self.name

def is_user_in_group(user, group):
  users = group.get_users()

  if len(users) < 1:
    return False
  if user in dict(zip(users, users)):
    return True
  else:
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

child.add_group(sub_child)
parent.add_group(child)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
print(is_user_in_group(sub_child_user, sub_child))
# True
sub_child.add_user('aa')
sub_child.add_user('bb')
sub_child.add_user('cc')
sub_child.add_user('dd')
sub_child.add_user('ee')
sub_child.add_user('ff')
print(is_user_in_group('gg', sub_child))
# False
print(is_user_in_group('', sub_child))
# False

