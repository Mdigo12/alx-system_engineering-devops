# create a file in /tmp with specific requirements

file { 'school': # resource type file and filename
  path    => '/tmp/school',
  mode    => '0744',   # file permissions
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet', # file content
}
