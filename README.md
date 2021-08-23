<!--- Please note that anything in between these tags is a comment. -->

## GeoEye
##### A simple little script/tool to help you obtain pinpoint accuracy in the free online game Geotastic.
<br />

## Ussage Steps
##### How to make it do the thing.

1. Go to the website https://geotastic.de/home and make a free account.

2. Make a local game or go online, it doesn't matter.

3. You will need to open your browsers dev tools console. `Ctrl + SHIFT + i` (Or what ever your buttons combination is for the browser you are using).

Should look something like this. (Firefox)
![2021-08-23_16-32](https://user-images.githubusercontent.com/45724082/130527879-ca1770ee-df10-48c8-91de-4a8eae0fc969.png)

4. Once here you will need to click on the "Network" tab and filter for "JS"
![2021-08-23_16-35](https://user-images.githubusercontent.com/45724082/130528137-c74f9405-40aa-4329-8c35-cc0f62797a38.png)

5. Then all you will need to do now is start up a match. If nothing shows up or you don't know what to click on. Close the dev console and repeat steps 3 & 4. Then  click the "Return to start" button in the window/game. After that you should get a result.
![2021-08-23_16-41](https://user-images.githubusercontent.com/45724082/130528648-ec21f0c4-3d1c-495a-a289-d54ddb65a471.png)

6. You will then need to right click that url highlighted in red. Hover over "Copy" then click on "Copy url".
7. Open up our nice little script and paste the url and hit enter. It will spit out some numbers and information. What we are interested in is what is highlighted in the red box. The numbers on the right are the lattitude and longitude and the information on the left will be our location/town name/country. (sometimes a road name/number).
![2021-08-23_16-45](https://user-images.githubusercontent.com/45724082/130529012-0000eddc-255a-4fe7-b835-a4a6732fc6b3.png)

8. From here we can just copy and paste the latitude and longitude numbers into google maps and then cross reference where we are with what se see on google maps for a perfect score.
<br />
<br />
<br />

## Additional Information
With this, I would like anyone to help contribute to this repo. If you know how to make the results we get via the google api get request then PLEASE by all means push a request.

If there are things you want done or added then please feel free to leave a suggestion or just straight up push a request.
I am making this repo to document how you can find your exact location on Geotastic as I currently could not find any other repos/code to help with this.
I look forward to seeing what you all can come up with! <3

<br />
<br />

## Note:
I am not liable, punishable, or responsible on or off platforms for those who use this code/method to cause damage or break things with the website. And I am in no way to be punished for what other people do.
