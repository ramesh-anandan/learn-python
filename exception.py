try:
    f = open('sample.log', 'w')
    f.write('Hello world')
except:
    print('File write failed!!')
else:
    print('file write success')
finally:
    print('file close')
    f.close()

print('hello')
