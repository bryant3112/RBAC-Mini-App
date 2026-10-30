RBAC and Authentication Mini-App

For this assignment, I created a basic Python application to demonstrate authentication and role-based access control (RBAC).

The program uses two accounts: an administrator and regular user. Each account has different permissions, and the program checks whether the user is authorized to access certain functions.

How my Program Works
1.- The admin account can access the Admin Dashboard but not the User Dashboard.
2.- The regular user can access the user DAshboard but not the Admin Dashboard. 
3.- An unknown username is denied access.

I also tested all three scenarios to make sure the program works correctly.

Understanding the CIA Triad 
Confidentiality: My program demonstrates confidentiality by limiting access based on user roles. This prevents regular users from accesing administrator functions.

Integrity: Role-based access control helps protect information by limiting who can perform ceratin actions. Although my project doesnt modify data, the same concept can help prevent unauthorized changes.

Availability: My application allows recognized users to access the functions assigned to their roles while the program is running.

What I learned 
This assignment helped me understand how authentication and authorization work together. I learned that recognizing a user and controlling what they can access are two different parts of application security.

This is simple educational simulation using hardcoded accounts, not a production-ready authentication system.