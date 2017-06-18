print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy?" % (
        age, height, weight)

### Another form
band = raw_input("What's your favorite band? ")
style = raw_input("What type of music do they play? ")
print "So ... you like the band %r and they play %r music?" %(
        band, style)
