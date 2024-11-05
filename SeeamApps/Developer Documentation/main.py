import tkinter as tk
from tkhtmlview import HTMLLabel

whay =('''
<html lang="en-US" foxified=""><head>
      <p><img src="https://codeberg.org/psyclown/SEEAM/raw/branch/main/assets/SeeamLogo.png" alt="drawing" width="200"></p>

<h1 id="seeam-docs">Seeam Docs</h1>
<p>Hello! and thank you for choosing Seeam! The worst way to distribute your files!</p>

<h1 id="table-of-contents">Table of Contents</h1>
<ol>
  <li><a href="#creating-a-new-app">Creating A New App</a></li>
  <li><a href="#already-made-apps">I Already Made My App!</a></li>
  <li><a href="#terms">Developer Terms Of Service</a></li>
</ol>

<h2 id="creating-a-new-app">Creating A New App<a class="anchorjs-link " href="#creating-a-new-app" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2>
<h4 id="requirements">Requirements<a class="anchorjs-link " href="#requirements" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>
<p>you will need either pipreqs, or a clean python installation.</p>
<h4 id="setup">Setup<a class="anchorjs-link " href="#setup" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h4>
<p>To setup your environment, you will need to set up a file structure like so:</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>myapp
│   description.txt
│   main.py    
│   thumbnail.png
│   requirements.txt
│   (optional) extras.py 
└───assets
</code></pre></div></div>
<p>The assets path will be where your program’s assets will be located.
(make sure the description doesn’t have too many lines or else it will be too long to display the play button)
<strong>Im pretty sure this is case-sensitive</strong></p>

<blockquote>
  <p>main.py is the main script that will be executed when your app is launched. 
<a href="#premade-apps">For Premade Apps</a>
extras.py is an <strong>OPTIONAL</strong> extra button on your apps launcher page, that will run extras.py. this is recommended to open a settings page, or run checks.
Thumbnail.png is the thumbnail of your app
description.txt is the description of your app</p>
</blockquote>

<h3 id="generating-installable-thingy">Generating Installable Thingy<a class="anchorjs-link " href="#generating-installable-thingy" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>
<h5 id="with-pipreqs">With pipreqs:<a class="anchorjs-link " href="#with-pipreqs" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h5>
<div class="language-powershell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="w">  </span><span class="n">pipreqs</span><span class="w"> </span><span class="s2">"/path/to/your/app"</span><span class="w">
</span></code></pre></div></div>
<h5 id="with-clean-install-or-venv">With clean install or venv<a class="anchorjs-link " href="#with-clean-install-or-venv" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h5>
<div class="language-powershell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">pip3</span><span class="w"> </span><span class="nx">freeze</span><span class="w"> </span><span class="err">&gt;</span><span class="w"> </span><span class="nx">requirements.txt</span><span class="w">
</span><span class="c">#this puts EVERYTHING pip has installed into requirements.txt</span><span class="w">
</span></code></pre></div></div>
<p>Finally, select all of the files, and compress them into a .zip file. upload this to somewhere online where you can get a direct download link, and there you go!</p>

<h2 id="already-made-apps">Already Made apps<a class="anchorjs-link " href="#already-made-apps" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2>
<p>You may want to redistribute an app as a seeam package to provide ease of installation to customers. this is pretty easy to do.</p>
<h3 id="windows-packages">Windows packages:<a class="anchorjs-link " href="#windows-packages" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>
<p>use this code in <code class="language-plaintext highlighter-rouge">main.py</code></p>
<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kn">import</span> <span class="nn">os</span>
<span class="n">os</span><span class="p">.</span><span class="n">startfile</span><span class="p">(</span><span class="s">"assets\example.exe"</span><span class="p">)</span>
</code></pre></div></div>
<h3 id="web-apps">Web apps<a class="anchorjs-link " href="#web-apps" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h3>
<p>webapps are a bit more customizable. here is the code snippet (<code class="language-plaintext highlighter-rouge">main.py</code>)</p>
<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="kn">from</span>  <span class="nn">tkinter</span>  <span class="kn">import</span>  <span class="o">*</span>
<span class="kn">import</span>  <span class="nn">webview</span>
<span class="kn">import</span>  <span class="nn">webview.window</span>
<span class="c1"># define an instance of tkinter
</span><span class="n">tk</span>  <span class="o">=</span>  <span class="n">Tk</span><span class="p">()</span>
<span class="c1"># size of the window where we show our website
</span><span class="n">tk</span><span class="p">.</span><span class="n">geometry</span><span class="p">(</span><span class="s">"1920x1080"</span><span class="p">)</span>
<span class="n">tk</span><span class="p">.</span><span class="n">attributes</span><span class="p">(</span><span class="s">'-fullscreen'</span><span class="p">,</span><span class="bp">True</span><span class="p">)</span>
<span class="c1"># Open website
</span><span class="n">webview</span><span class="p">.</span><span class="n">create_window</span><span class="p">(</span><span class="s">'Google'</span><span class="p">,</span> <span class="s">'https://google.com'</span><span class="p">,</span> <span class="n">fullscreen</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
<span class="n">webview</span><span class="p">.</span><span class="n">start</span><span class="p">()</span>
</code></pre></div></div>
<h2 id="terms">Terms<a class="anchorjs-link " href="#terms" aria-label="Anchor" data-anchorjs-icon="" style="font: 1em / 1 anchorjs-icons; padding-left: 0.375em;"></a></h2>
<p>Yeah basically if you make anything that will interact with the users system in a way that is not very specifically described on your website, then you <em>WILL</em> be blacklisted from our servers when we actually make them. 
Also dont make any of these:</p>

<ul>
  <li>Viruses</li>
  <li>Crypto mining in any way</li>
  <li>interacting with SEEAM’s files</li>
  <li>interacting with system files in a way that is harmful to the user’s device</li>
  <li>AND NO NSFW (no sus visual novels!!!😁)</li>
</ul>


      
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/anchor-js/4.1.0/anchor.min.js" integrity="sha256-lZaRhKri35AyJSypXXs4o6OPFTbTmUoltBbDCbdzegg=" crossorigin="anonymous"></script>
    <script>anchors.add();</script>
  

</body></html>
''')

root = tk.Tk()
html_label = HTMLLabel(root, html=whay)
html_label.pack(fill="both", expand=True)
root.title("Epic App Launcher")
root.geometry("1280x720")
root.mainloop()
print(whay)