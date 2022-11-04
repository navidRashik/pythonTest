# Solved errors

## 1

```
RuntimeError: Model class movies.models.Movie doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
```

## 2

prob:

```
❯ http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"

HTTP/1.1 404 Not Found
Content-Length: 2119
Content-Type: text/html
Date: Fri, 04 Nov 2022 16:35:18 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.9.7
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <title>Page not found at /api/v1/auth/register/</title>
  <meta name="robots" content="NONE,NOARCHIVE">
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; background:#eee; color:#000; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; margin-bottom:.4em; }
    h1 span { font-size:60%; color:#666; font-weight:normal; }
    table { border:none; border-collapse: collapse; width:100%; }
    td, th { vertical-align:top; padding:2px 3px; }
    th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    #info { background:#f6f6f6; }
    #info ol { margin: 0.5em 4em; }
    #info ol li { font-family: monospace; }
    #summary { background: #ffc; }
    #explanation { background:#eee; border-bottom: 0px none; }
  </style>
</head>
<body>
  <div id="summary">
    <h1>Page not found <span>(404)</span></h1>
    <table class="meta">
      <tr>
        <th>Request Method:</th>
        <td>POST</td>
      </tr>
      <tr>
        <th>Request URL:</th>
        <td>http://127.0.0.1:8000/api/v1/auth/register/</td>
      </tr>
      
    </table>
  </div>
  <div id="info">
    
      <p>
      Using the URLconf defined in <code>api_crud.urls</code>,
      Django tried these URL patterns, in this order:
      </p>
      <ol>
        
          <li>
            
                api/v1/movies/
                
            
          </li>
        
          <li>
            
                admin/
                
            
          </li>
        
      </ol>
      <p>
        
        The current path, <code>api/v1/auth/register/</code>, didn't match any of these.
      </p>
    
  </div>

  <div id="explanation">
    <p>
      You're seeing this error because you have <code>DEBUG = True</code> in
      your Django settings file. Change that to <code>False</code>, and Django
      will display a standard 404 page.
    </p>
  </div>
</body>
</html>

```

sol: added to urls

prob:

```
    from authentication.views import RegisterView
  File "/home/navid/Downloads/Selise Python Developer Assessment - Final/InterviewExam/authentication/views.py", line 4, in <module>
    from .serializers import RegisterSerializer
  File "/home/navid/Downloads/Selise Python Developer Assessment - Final/InterviewExam/authentication/serializers.py", line 7, in <module>
    class RegisterSerializer(serializers.ModelSerializer):
  File "/home/navid/Downloads/Selise Python Developer Assessment - Final/InterviewExam/authentication/serializers.py", line 13, in RegisterSerializer
    password = serializers.CharField(
  File "/home/navid/Downloads/Selise Python Developer Assessment - Final/InterviewExam/venv/lib/python3.9/site-packages/rest_framework/fields.py", line 778, in __init__
    super().__init__(**kwargs)
  File "/home/navid/Downloads/Selise Python Developer Assessment - Final/InterviewExam/venv/lib/python3.9/site-packages/rest_framework/fields.py", line 336, in __init__
    assert not (read_only and required), NOT_READ_ONLY_REQUIRED
AssertionError: May not set both `read_only` and `required`

```

sol: removed read only as we need to set password through this serializer

## 3

```
http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"
HTTP/1.1 401 Unauthorized
Allow: POST, OPTIONS
Content-Length: 58
Content-Type: application/json
Date: Fri, 04 Nov 2022 16:49:22 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.9.7
Vary: Accept
WWW-Authenticate: Bearer realm="api"
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "detail": "Authentication credentials were not provided."
}


❯ http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD" password2="PASSWORD"
HTTP/1.1 400 Bad Request
Allow: POST, OPTIONS
Content-Length: 40
Content-Type: application/json
Date: Fri, 04 Nov 2022 16:50:44 GMT
Referrer-Policy: same-origin
Server: WSGIServer/0.2 CPython/3.9.7
Vary: Accept
X-Content-Type-Options: nosniff
X-Frame-Options: DENY

{
    "password": [
        "This field is required."
    ]
}
```

sol: Allowany, chaged source and updated reciving variable of the serializer

prob:

```

# if attrs['password'] == attrs['password2']:
        #     raise serializers.ValidationError(
        #         {"password": "Password fields didn't match."})

```

sol:removed wrong validations

prb:

```

Got AttributeError when attempting to get a value for field `password2` on serializer `RegisterSerializer`.
The serializer field might be named incorrectly and not match any attribute or key on the `User` instance.
Original exception text was: 'User' object has no attribute 'password2'.

Request Method:  POST
Request URL:  <http://127.0.0.1:8000/api/v1/auth/register/>

```

sol: password2 converted to write only field and same for password1

## 4

prb: following was wroking without token

```

http  <http://127.0.0.1:8000/api/v1/movies/>

```

sol:  permissions.IsAuthenticated

prob: everyone was updating and deleting movies
sol: added following block

```
 def get_queryset(self):
        if self.request.method != 'GET':
            self.queryset = Movie.objects.filter(creator=self.request.user)
        return super().get_queryset()
```
## 5
prob: CustomPagination
wrong class variable name 
## 6
fix MovieFilter : filter was broken 