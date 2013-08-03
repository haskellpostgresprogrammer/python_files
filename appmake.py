import umarutils as u
import os

def quotesfile(qf):
    a = "".join(u.readfile(qf)[:-1]).split("\n\n")
    b = [x.split("\n") for x in a]
    for x in b:
        x.insert(-1,"--")
    c = ["".join(x) for x in b]
    return c
    
def javaarray(l):
    return "\n".join(["".join(["d[",str(x[0]),"] = \"",x[1],"\";"])
                      for x in zip(range(len(l)),l)])

def javafile(arraydata,packagename):
    return """package """+packagename+""".android;

import android.app.Activity;
import android.os.Bundle;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Button;
import android.view.View.OnClickListener;
import android.view.View;
import android.graphics.PorterDuff;
import android.graphics.Color;
import java.util.Random;
import android.view.Gravity;
import com.google.ads.*;

public class """+packagename+""" extends Activity
{
    private AdView ad;

    /** Called when the activity is first created. */

    @Override
    public void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
	LinearLayout ll = new LinearLayout(this);
	ll.setOrientation(LinearLayout.VERTICAL);
	final TextView tv = new TextView(this);
	tv.setGravity(Gravity.CENTER);
	Button b = new Button(this);
	b.getBackground().setColorFilter(Color.GREEN,
					 PorterDuff.Mode.MULTIPLY);

	final Random random = new Random();

	final String[] d = new String[100];
"""+arraydata+"""

	b.setOnClickListener(new OnClickListener () {
		public void onClick(View v) {
		    int r = random.nextInt(100);
		    tv.setText(d[r]);
		}
	    });

	int ri = random.nextInt(100);
	tv.setText(d[ri]);

	ad = new AdView(this, AdSize.BANNER, "a14f1d56880f564");
	ll.addView(ad);

	ll.addView(b);
	ll.addView(tv);
        setContentView(ll);

	ad.loadAd(new AdRequest());

    }

    @Override
	public void onDestroy() {
	ad.destroy();
	super.onDestroy();
    }

}
"""

def writejavafile(infile,outfile,name):
    u.writefile(javafile(javaarray(quotesfile(infile)),name),outfile)

writejavafile("/home/umar/quoteapps/intelligence",
              "/home/umar/123","ncbi")

def quoteapps():
    return [x
            for x in os.listdir("/home/umar/quoteapps")
            if x.endswith("~") != True]

def manifestfile(name,filepath):
    a = """<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
      package=" """+name+""".android"
      android:versionCode="1"
      android:versionName="1.0">
  <application android:label="@string/app_name"
		 android:icon="@drawable/icon" >
        <activity android:name="""+"\""+name+"\""+"""
                  android:label="@string/app_name">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
	<activity android:name="com.google.ads.AdActivity"
		  android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|uiMode|screenSize|smallestScreenSize"/>

    </application>
	<uses-permission android:name="android.permission.INTERNET"/>
	<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>


	<uses-sdk 
	    android:minSdkVersion="7" 
	    android:targetSdkVersion="15" 
	    />

</manifest> 
"""
    u.writefile(a,filepath+"/AndroidManifest.xml")

def buildxmlfile(name,filepath):
    a = """<?xml version="1.0" encoding="UTF-8"?>
<project name="""+"\""+name+"\""+""" default="help">

    <!-- The local.properties file is created and updated by the 'android' tool.
         It contains the path to the SDK. It should *NOT* be checked into
         Version Control Systems. -->
    <property file="local.properties" />

    <!-- The ant.properties file can be created by you. It is only edited by the
         'android' tool to add properties to it.
         This is the place to change some Ant specific build properties.
         Here are some properties you may want to change/update:

         source.dir
             The name of the source directory. Default is 'src'.
         out.dir
             The name of the output directory. Default is 'bin'.

         For other overridable properties, look at the beginning of the rules
         files in the SDK, at tools/ant/build.xml

         Properties related to the SDK location or the project target should
         be updated using the 'android' tool with the 'update' action.

         This file is an integral part of the build system for your
         application and should be checked into Version Control Systems.

         -->
    <property file="ant.properties" />

    <!-- The project.properties file is created and updated by the 'android'
         tool, as well as ADT.

         This contains project specific properties such as project target, and library
         dependencies. Lower level build properties are stored in ant.properties
         (or in .classpath for Eclipse projects).

         This file is an integral part of the build system for your
         application and should be checked into Version Control Systems. -->
    <loadproperties srcFile="project.properties" />

    <!-- quick check on sdk.dir -->
    <fail
            message="sdk.dir is missing. Make sure to generate local.properties using 'android update project' or to inject it through an env var"
            unless="sdk.dir"
    />


<!-- extension targets. Uncomment the ones where you want to do custom work
     in between standard targets -->
<!--
    <target name="-pre-build">
    </target>
    <target name="-pre-compile">
    </target>

    /* This is typically used for code obfuscation.
       Compiled code location: ${out.classes.absolute.dir}
       If this is not done in place, override ${out.dex.input.absolute.dir} */
    <target name="-post-compile">
    </target>
-->

    <!-- Import the actual build file.

         To customize existing targets, there are two options:
         - Customize only one target:
             - copy/paste the target into this file, *before* the
               <import> task.
             - customize it to your needs.
         - Customize the whole content of build.xml
             - copy/paste the content of the rules files (minus the top node)
               into this file, replacing the <import> task.
             - customize to your needs.

         ***********************
         ****** IMPORTANT ******
         ***********************
         In all cases you must update the value of version-tag below to read 'custom' instead of an integer,
         in order to avoid having your file be overridden by tools such as "android update project"
    -->
    <!-- version-tag: 1 -->
    <import file="${sdk.dir}/tools/ant/build.xml" />


</project>

    """
    u.writefile(a,filepath+"/build.xml")

import shutil
def makeapptree(name):
    shutil.copytree("/home/umar/apptemplate",
                    "/home/umar/"+name)
    
def makeappfiles(n):
    name = n+"quotes"
    makeapptree(name)
    buildxmlfile(name,"/home/umar/"+name)
    manifestfile(name,"/home/umar/"+name)
    shutil.rmtree("".join(["/home/umar/",name,"/src/","ncbi"]))
    os.makedirs("".join(["/home/umar/",name,
                             "/src/",name,"/android/"]))
    writejavafile("/home/umar/quoteapps/"+n,
                  "".join(["/home/umar/",name,
                           "/src/",name,"/android/",name,".java"]),
                  name)

def removeappfilestree(n):
    name = n+"quotes"
    shutil.rmtree("/home/umar/"+name)

def makeapps():
    for x in quoteapps():
        makeappfiles(x)
    
def removeapps():
    for x in quoteapps():
        removeappfilestree(x)
