# Puppet script to +se the requests the serve can handle

exec { 'edit_conf_lim':
    command => 'sed -i "s/15/4096/g" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
}

# restart nginx if conf has been edited
exec { 'restart_nginx':
    command => 'nginx restart',
    path    => '/etc/init.d/',
    require => Exec['edit_conf_lim']
}
