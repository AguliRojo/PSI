#basic formatting
'{} {}'.format('one', 'two')    #old
'%s %s' % ('one', 'two')        #new

#setup value conversion
class Data(object):

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

'%s %r' % (Data(), Data())      #old
'{0!s} {0!r}'.format(Data())    #new

#padding and alligning strings
'%10s' % ('test',)              #old
'{:>10}'.format('test')         #new

#padding and alligning strings (left allign)
'%-10s' % ('test',)             #old
'{:10}'.format('test')          #new

#numbers
'%d' % (42,)                    #old
'{:d}'.format(42)               #new

