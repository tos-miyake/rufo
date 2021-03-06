#~# ORIGINAL
#~# spaces_around_equal: :one

a=1

#~# EXPECTED

a = 1

#~# ORIGINAL
#~# spaces_around_equal: :one

a  =  1

#~# EXPECTED

a = 1

#~# ORIGINAL
#~# spaces_around_equal: :dynamic, align_assignments: true

a  =  1

#~# EXPECTED

a = 1

#~# ORIGINAL
#~# spaces_around_equal: :one, align_assignments: true

a  =  1

#~# EXPECTED

a = 1

#~# ORIGINAL
#~# spaces_around_equal: :one

a+=1

#~# EXPECTED

a += 1

#~# ORIGINAL
#~# spaces_around_equal: :one

a  +=  1

#~# EXPECTED

a += 1

#~# ORIGINAL
#~# spaces_around_equal: :dynamic, align_assignments: true

a  +=  1

#~# EXPECTED

a += 1

#~# ORIGINAL
#~# spaces_around_equal: :one, align_assignments: true

a  +=  1

#~# EXPECTED

a += 1

#~# ORIGINAL
#~# spaces_around_equal: :one

def foo(x  =  1)
end

#~# EXPECTED

def foo(x = 1)
end

#~# ORIGINAL
#~# spaces_around_equal: :one

def foo(x=1)
end

#~# EXPECTED

def foo(x = 1)
end

#~# ORIGINAL
#~# spaces_around_equal: :dynamic

def foo(x  =  1)
end

#~# EXPECTED

def foo(x  =  1)
end

#~# ORIGINAL
#~# spaces_around_equal: :dynamic

def foo(x=1)
end

#~# EXPECTED

def foo(x=1)
end

