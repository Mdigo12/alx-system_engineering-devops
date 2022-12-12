# install install flask from pip3 using Puppet

exec { 'install python packages':
  command => 'pip3 install flask==2.1.0 Werkzeug==2.1.1 flask_restful apiai',
  path    => ['/usr/bin/'],
  unless  => '/usr/bin/test -f /usr/local/lib/python3.8.10/dist-packages/flask/app.py',
}
