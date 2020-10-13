def buildProfile(first, last, **userInfo):
    '''Build a dictionary containing everything we know about a user.'''
    profile = {}
    profile['firstName'] = first
    profile['lastName'] = last
    for key, value in userInfo.items():
        profile[key] = value
    return profile

userProfile = buildProfile('albert', 'einstein', 
                            location='princeton',
                            feild='physics')

print(userProfile)

me = buildProfile('eric', 't',
                location='h-town',
                feild='programing',
                )
print(me)