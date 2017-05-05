from fabric.api import local

def test():
  local("cd /home/visualpath/Documents/python/fabric/git_import/fabric_test_project && python manage.py")
def commit():
  local("cd /home/visualpath/Documents/python/fabric/git_import/fabric_test_project && git add . && git commit -m 'testing 123' ")
def push():
  local("cd /home/visualpath/Documents/python/fabric/git_import/fabric_test_project && git push origin master")
def pull():
  local("cd /home/visualpath/Documents/python/fabric/git_import/fabric_test_project && git pull")

def deploy():
  print "Executing manage script."
  print "------------------------"
  test()
  print "Commiting git code locally."
  print "---------------------------"
  commit()
  print "Pushing local git repository to Github."
  print "---------------------------------------"
  push()
  print "Pulling from local git repository to Github."
  print "--------------------------------------------"
  pull()

