# A puppet script to replace rewrite a line

$path_file = '/var/www/html/wp-settings.php'

#rewrite "phpp" to "php"

exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${path_file}",
  path    => ['/bin','/usr/bin']
}
