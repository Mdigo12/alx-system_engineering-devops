# Using Puppet, install flask from pip3

exec { 'install python packages':
  command => 'pip3 install flask flask_restful apiai',
  path    => ['/usr/bin/'],
  unless  => '/usr/bin/test -f /usr/local/lib/python3.8.10/dist-packages/flask/app.py',
}
