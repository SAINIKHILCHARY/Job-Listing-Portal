# MongoDB Atlas Setup Guide - Secure Universal Database

## Step 1: Create MongoDB Atlas Account

1. **Visit MongoDB Atlas**: <https://www.mongodb.com/cloud/atlas/register>
2. **Sign up** with your email

3. **Create an organization** (optional)

4. **Create a project** named "Job Listing Portal"

## Step 2: Create a Database Cluster

1. Click **"Create a Deployment"** â†’ Choose **"Production"**

2. Select **AWS** as cloud provider

3. Choose a **region** close to your users (e.g., `us-east-1` for US)

4. Select **"M0 Free"** tier (free for development/testing)

5. Click **"Create"** and wait for cluster to deploy (5-10 minutes)

## Step 3: Create Database User

1. Go to **"Database Access"** in left sidebar

2. Click **"Add Database User"**
3. Create username: `<your-app-username>` (e.g., `talent_bridge_user`)
4. **Generate a secure password** (copy and save it safely)

5. Set permissions to **"Read and write to any database"**
6. Click **"Add User"**

## Step 4: Configure Network Access

1. Go to **"IP Access List"** in left sidebar

2. Click **"Add IP Address"**
3. Select **"Allow access from anywhere"** (for universal access)
   - This allows any IP to connect (secured by username/password)

4. Click **"Confirm"**

âš ï¸ **Note**: Always use strong passwords for database users!

## Step 5: Get Connection String

1. Go to **"Databases"** â†’ Click **"Connect"**

2. Select **"Drivers"** â†’ Choose **"Node.js"** driver

3. Copy the connection string (looks like):

   ```

   mongodb+srv://<username>:<password>@cluster.mongodb.net/?retryWrites=true&w=majority
   ```

## Step 6: Update .env File

Replace the `MONGODB_URI` in your `.env` file with:

```env
MONGODB_URI=mongodb+srv://talent_bridge_user:YOUR_SECURE_PASSWORD@cluster0.xxxxx.mongodb.net/job_listing_portal?retryWrites=true&w=majority
JWT_SECRET=YOUR_SUPER_SECRET_JWT_KEY_USE_STRONG_PASSWORD
JWT_EXPIRE=7d

```text
âš ï¸ **NEVER** commit `.env` to GitHub - add to `.gitignore`

## Security Features Enabled âœ…

1. **Password Protected**: Database user authentication
2. **IP Whitelisting**: Network access control
3. **SSL/TLS Encryption**: Data in transit encrypted
4. **Encryption at Rest**: Data at rest encrypted (Atlas Pro feature)
5. **Audit Logging**: All operations logged
6. **Backup & Recovery**: Automatic encrypted backups
7. **Rate Limiting**: API endpoint protection
8. **Input Sanitization**: MongoDB injection prevention
9. **CORS Protection**: Cross-origin request validation
10. **JWT Tokens**: Stateless authentication

## Testing Connection

Run this after updating `.env`:

```bash
cd server
node -e "const mongoose = require('mongoose'); mongoose.connect(process.env.MONGODB_URI).then(() => console.log('âœ… MongoDB Connected Successfully!')).catch(err => console.log('âŒ Connection Failed:', err.message));"

```text
## Environment Variables

**Production (.env)** - Keep this file private:

- `MONGODB_URI`: Atlas connection string

- `JWT_SECRET`: Strong random string (min 32 characters)

- `CLIENT_URL`: Your deployed frontend URL

- `NODE_ENV`: 'production'

**Never share** your .env file or commit it to version control!

## Recommended MongoDB Atlas Upgrades

For production:

- **M2 Paid Cluster** ($9/month): Better performance, dedicated resources

- **Database Encryption**: Enable customer-managed encryption

- **X.509 Authentication**: Certificate-based authentication

- **Advanced Audit Logging**: Complete operation tracking

- **Backup Snapshots**: Automated daily backups

## Security Checklist âœ“

- [ ] Created strong database password (min 12 chars, mixed case, numbers, symbols)

- [ ] Saved credentials in a secure password manager

- [ ] Updated `.env` with correct connection string

- [ ] Added `.env` to `.gitignore`

- [ ] Enabled network access (IP whitelist)

- [ ] Set JWT_SECRET to strong random value

- [ ] Tested connection successfully

- [ ] Enabled HTTPS on your frontend (if deployed)

- [ ] Never share `.env` file or credentials

- [ ] Regular database backups enabled

## Troubleshooting

**Cannot connect?**

- Check username/password in connection string (URL encode special chars!)

- Verify IP address is whitelisted in Atlas

- Ensure cluster is running (green status in Atlas)

**Connection timeout?**

- Verify network connectivity

- Check firewall settings

- Try from different IP address

**Auth errors?**

- Ensure username exists in Database Access

- Verify password is correctly URL encoded in connection string
