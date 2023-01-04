verb = "eat"
noun = "Eggs Benedict with York ham"

print("I want to " + verb + " " + noun)
print("I want to %s %s" % (verb, noun))
print("I want to %s %s" % ("eat", noun))
print("I want to {0} {1}".format(verb, noun))
print("I want to {smt_you_want_to_do} {smt_you_want_to_do_it_with}"
      .format(smt_you_want_to_do=verb, smt_you_want_to_do_it_with=noun))
