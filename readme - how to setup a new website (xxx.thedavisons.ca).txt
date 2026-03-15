Instructions on how to setup new website (May 2015)

Webnames.ca is the company that holds the registration for the domains www.thedavisons.ca and www.hbhomes.ca
Amazon hosts a static website for both the davisons.ca and hbhomes.ca
You need to point the names servers for both domains to the aws name servers


1. create (or copy) root directory under C:\Users\rdavison\Documents\Rons Documents\Rons Personal Stuff\Webs
2. Login into AWS webhosting.
3. Goto S3 - storage in the cloud
4. Create a new bucket - call it xxx.thedavisons.ca where xxx is what you creating
5. Add bucket permissions by adding a bucket policy - coyp this from another site
6. enable static website hosting (this done on properties tab of the bucket once it has been created)

7. Goto Route 53 - DNS and domain name registration
The DNS part (CNAME) has been changed to Cloudflare (login using google). Basically the same as S3 but changed to use something similar to NGROK to run wordle and wireguard monitor
8. Click on hosted zones and then click on thedavisons.ca
9. You will see all the CNAME records - create one for your website
10. you will need to copy the endpoint (you can get it from the set 4 above) and put it in the CNAME value (e.g. case.thedavisons.ca.s3-website-us-west-2.amazonaws.com) 
11. save - you will have to wait for a bit before you can access 

12. go to cloudberry sync and setup folders to sync with S3




============= bucket policy below - saves from having to open another webiste =========

{
	"Version": "2012-10-17",
	"Statement": [
		{
			"Sid": "AddPerm",
			"Effect": "Allow",
			"Principal": "*",
			"Action": "s3:GetObject",
			"Resource": "arn:aws:s3:::boat.thedavisons.ca/*"
		}
	]
}

