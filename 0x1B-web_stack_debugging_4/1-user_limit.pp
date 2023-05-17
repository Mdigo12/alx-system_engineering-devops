# puppet script to change the OS configuration
# so that it is possible to login with the holberton user
# and open a file without any error message.
# These lines set the soft and hard limits for the maximum number of open file descriptors to 50000.

exec { 'editing_the_hard_and_soft_limits':
  command => 'sed -i "/holberton hard nofile/s/5/50000/; /holberton soft nofile/s/4/60000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
