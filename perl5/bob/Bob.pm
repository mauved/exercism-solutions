#
# This is a SKELETON file and has been provided to enable you to get working on the
# first exercise more quickly.
# Completed by Sofia Nieves
# Sun 29 May 07:17:56 UTC 2016
#

use 5.006;
use strict;
use warnings;

package Bob;

our $VERSION = '1.000';

use Exporter 5.57 qw(import);

our @EXPORT_OK = qw(hey);

sub hey {
    my ($banter) = @_;

    # Check for only invisible characters
    if ($banter =~ /^\p{Separator}*$/) {
        return 'Fine. Be that way!';
    }

    # Check for lack of lower case letters
    if ($banter =~ /\p{Letter}/ and $banter !~ /\p{Lowercase_Letter}/) {
        return 'Whoa, chill out!';
    }

    # Check for a question
    if ($banter =~ /.*\?$/) {
        return 'Sure.';
    }

    return 'Whatever.';
}

1;
