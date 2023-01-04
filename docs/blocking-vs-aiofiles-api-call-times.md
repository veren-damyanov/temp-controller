
```
yassen@cougar:~/Work/Yassens/temp-controller$ time curl http://92.247.54.152:8000/temperature
{"sensor_data":[{"sensor-id":"28-01186e4edfff","sensor-name":"RAID-CONTROLLER","raw-temp":28937,"adjusted-temp":null},{"sensor-id":"28-0417333777ff","sensor-name":"RPI-AREA","raw-temp":23750,"adjusted-temp":null},{"sensor-id":"28-3c01d0751078","sensor-name":"RAM-AREA","raw-temp":27437,"adjusted-temp":null},{"sensor-id":"28-3c01d075ed82","sensor-name":"CASE","raw-temp":28875,"adjusted-temp":null}]}
real	0m3,671s
user	0m0,003s
sys	0m0,004s
```

```
yassen@cougar:~/Work/Yassens/temp-controller$ time curl http://92.247.54.152:8000/temperature
{"sensor_data":[{"sensor-id":"28-01186e4edfff","sensor-name":"RAID-CONTROLLER","raw-temp":28937,"adjusted-temp":null},{"sensor-id":"28-0417333777ff","sensor-name":"RPI-AREA","raw-temp":23750,"adjusted-temp":null},{"sensor-id":"28-3c01d0751078","sensor-name":"RAM-AREA","raw-temp":27437,"adjusted-temp":null},{"sensor-id":"28-3c01d075ed82","sensor-name":"CASE","raw-temp":28875,"adjusted-temp":null}]}
real	0m3,620s
user	0m0,004s
sys	0m0,004s
```

```
yassen@cougar:~/Work/Yassens/temp-controller$ time curl http://92.247.54.152:8000/temperature
{"sensor_data":[{"sensor-id":"28-01186e4edfff","sensor-name":"RAID-CONTROLLER","raw-temp":29000,"adjusted-temp":null},{"sensor-id":"28-0417333777ff","sensor-name":"RPI-AREA","raw-temp":23750,"adjusted-temp":null},{"sensor-id":"28-3c01d0751078","sensor-name":"RAM-AREA","raw-temp":27500,"adjusted-temp":null},{"sensor-id":"28-3c01d075ed82","sensor-name":"CASE","raw-temp":28937,"adjusted-temp":null}]}
real	0m3,720s
user	0m0,000s
sys	0m0,008s
```

After making it truly async using :

```
yassen@cougar:~$ time curl http://92.247.54.152:8000/temperature
{"sensor-data":[{"sensor-id":"28-01186e4edfff","sensor-name":"RAID-CONTROLLER","raw-temp":28625,"adjusted-temp":null},{"sensor-id":"28-0417333777ff","sensor-name":"RPI-AREA","raw-temp":23312,"adjusted-temp":null},{"sensor-id":"28-3c01d0751078","sensor-name":"RAM-AREA","raw-temp":27125,"adjusted-temp":null},{"sensor-id":"28-3c01d075ed82","sensor-name":"CASE","raw-temp":28562,"adjusted-temp":null}]}
real	0m1,177s
user	0m0,003s
sys	0m0,005s
```