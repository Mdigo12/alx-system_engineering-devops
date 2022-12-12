file { 'school': # resource type file and filename
  path    => '/etc/school',
  mode    => '0744',   # file permissions
  owner   => 'www-data',
  group   => 'www-data',
  content => "I love Puppet\n", # file content
}
