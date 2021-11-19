# Deploying Python container App

## Heroku Deployment

### Heroku Login

<div class="termy">

```console
$ heroku login -i
$ heroku container:login

```
</div>

### Heroku Create app

<div class="termy">

```console
$ heroku create pyapp-abhi

Creating ⬢ pyapp-abhi... done
https://pyapp-abhi.herokuapp.com/ | https://git.heroku.com/pyapp-abhi.git
```
</div>

### Heroku Push app

<div class="termy">

```console
$ heroku container:push web --app pyapp-abhi

=== Building web (Dockerfile)
[+] Building 0.7s (10/10) FINISHED
=== Pushing web (Dockerfile)
Using default tag: latest
Your image has been successfully pushed. You can now release it with the 'container:release' command.
```
</div>

### Heroku Release app

<div class="termy">

```console
$ heroku container:release web --app pyapp-abhi

Releasing images web to pyapp-abhi... done
```
</div>
### Check it

Open your browser at <a href="https://pyapp-abhi.herokuapp.com" class="external-link" target="_blank">https://pyapp-abhi.herokuapp.com</a>.

You will see the JSON response as:

```JSON
{"message": "Hello Bigger Applications!"}
```

### Yay! It worked !!


### Delete app from Heroku
<div class="termy">

```console
$  heroku apps:destroy -a pyapp-abhi --confirm pyapp-abhi

Destroying ⬢ pyapp-abhi (including all add-ons)... done
```
</div>