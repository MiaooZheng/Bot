# checkout bot

***For this project, I'm going to make a checkout bot to purchase the shoes. As the size i want is unavailable right now, i'll try to connect with email notifications or use airflow to check whether item is available per hour***

** Update on May29,2023**
- As my item is available and I have already purchased it. I just stopped at the step of adding payment method. (coz this item is not $20, i don't want to pay and do a return. But the codes for the add payment info are very similar as before. :) )

Now I have done the automation of searching product and proceeding to checkout and also sending email. 

The next step:
- i'll use airflow to do a toy project. - check website per hour, if item available, send email/sms. (Notes: if you're using fido/rogers in Canada, you need to subscribe this service ($5/month :(()

Other steps/ideas may keep coming.. (But probably that's all for this project💁


** Update on May23,2023
- I'm thinking to do automation to check availability and if yes, send text message. However, I encountered some issues:
>> email to text_message file done. It works for US ATT and Canada Bell and Telus. However, I'm using fido as mobile carrier, which is not free at this time. So may not be able to send text to my own phone no. when it has stock. 

Plan for next step: 
- Since my friend told me there maybe delays from store email. I may still want to send email to my email address if i find it's in stock. 
- Use airflow to do automation. 


--------------------
Current plan: 
- finish the rest of code, choose size, add to cart and checkout. (done)
- connect to email and when I receive notification from store, run the above code immediately. 
- use airflow to automatically check availability per 30mins and buy if available. 
