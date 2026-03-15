March 2026.

So i re-organized everything.

1. Webnames.ca only holds the domain names (www.thedavisons.ca & www.hbhomes.ca)
2. Cloudflare handles the DNS and allows sites to operate with a certificate (ssl/https)
3. All websites are under C:\Rons Documents\Rons Personal Stuff\repo-websites
4. All websites are stored in GitHub
5. GitHub (under the hbhomes.ca) repository has been setup with a pipeline to push any changes to Amazon S3
6. Web sites all built with prompt programing using ChatGPT
7. If you want to create a new website (xxx.thedavisons.ca or xxx.hbhomes.ca) you need to create the S3 Bucket in amazon and that should be it.  


