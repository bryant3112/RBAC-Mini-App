# RBAC and Authentication Mini-App
# Demonstrates  role-based access control in Python. 


users = {
    "admin123": "admin",
    "employee123": "user"
}

def admin_dashboard(role):
    if role == "admin":
        print("Access granted: Admin Dashboard")
    else:
        print("Access denied: Admins only.")

def user_dashboard(role):
    if role == "user":
        print("Access granted: User Dashboard")
    else:
        print("Access denied: Users only.")

def login(username):
    if username not in users:
        print("Login failed: Username not found.")
        return

    role = users[username]
    print(f"Login successful: {username}")
    print(f"Assigned role: {role}")

    admin_dashboard(role)
    user_dashboard(role)

login("admin123")
print("--------------------")
login("employee123")
print("--------------------")
login("unknown")                             

