# GitHub Pages Setup Guide

This guide explains how to enable GitHub Pages for your messaging epic documentation.

## 🚀 Quick Setup (5 minutes)

### Step 1: Enable GitHub Pages

1. Go to your repository: https://github.com/jerryagenyi/sul-messaging-epic
2. Click **Settings** tab
3. Scroll down to **Pages** section (left sidebar)
4. Under **Source**, select **GitHub Actions**
5. Click **Save**

### Step 2: Enable Required Permissions

1. Still in **Settings**, go to **Actions** → **General**
2. Scroll to **Workflow permissions**
3. Select **Read and write permissions**
4. Check **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

### Step 3: Trigger Deployment

Push any change to the master branch, or manually trigger the workflow:

1. Go to **Actions** tab
2. Click **CI/CD Pipeline**
3. Click **Run workflow** → **Run workflow**

## 📍 **Where to View Documentation**

Once setup is complete, your documentation will be available at:

### **🌐 Live Documentation Site**
```
https://jerryagenyi.github.io/sul-messaging-epic/
```

### **📊 What You'll See**

The documentation site will include:

#### **1. Project Overview**
- Repository information
- Test coverage summary
- Development approach explanation

#### **2. Specifications**
- Feature specifications from `docs/specs/`
- Gherkin test scenarios from `docs/gherkin/`
- Test matrix from `docs/testing/`

#### **3. Test Reports**
- Latest test execution results
- HTML test reports with screenshots
- Test coverage metrics
- CI/CD pipeline status

#### **4. Development Guide**
- Complete TDD workflow
- Step-by-step implementation roadmap
- Code examples and best practices
- API endpoint suggestions

## 🔄 **Automatic Updates**

The documentation site will automatically update when:
- ✅ You push changes to the master branch
- ✅ Tests run and generate new reports
- ✅ Documentation files are modified
- ✅ New features are implemented

## 📱 **Mobile-Friendly Design**

The documentation site is responsive and works on:
- 💻 Desktop browsers
- 📱 Mobile devices
- 📊 Tablets
- 🖥️ Large screens

## 🎯 **Use Cases**

### **For Developers**
- Access TDD development guide
- View test requirements and specifications
- Check latest test results
- Reference API documentation

### **For Stakeholders**
- Review project progress
- Understand feature requirements
- View test coverage and quality metrics
- Access formatted specifications

### **For QA Teams**
- Review test matrices and scenarios
- Access test reports and results
- Understand acceptance criteria
- Track testing progress

### **For Management**
- Monitor project status
- Review quality metrics
- Access professional project documentation
- Share progress with external stakeholders

## 🛠️ **Customization Options**

You can customize the documentation by:

### **1. Modifying the HTML Template**
Edit the HTML in `.github/workflows/ci.yml` under "Create documentation site"

### **2. Adding Custom Styles**
Update the CSS in the `<style>` section

### **3. Including Additional Content**
- Add more markdown files
- Include images and diagrams
- Embed test videos or screenshots

### **4. Custom Domain (Optional)**
Set up a custom domain like `docs.yourdomain.com`:
1. Add `CNAME` file to docs-site folder
2. Configure DNS settings
3. Update repository settings

## 🔍 **Troubleshooting**

### **Pages Not Deploying?**
1. Check **Actions** tab for deployment errors
2. Verify **Pages** is set to **GitHub Actions** source
3. Ensure workflow permissions are correct

### **404 Error?**
1. Wait 5-10 minutes after first deployment
2. Check if repository is public
3. Verify the URL format

### **Missing Content?**
1. Check if files exist in repository
2. Review workflow logs in **Actions** tab
3. Ensure markdown files are properly formatted

## 📈 **Analytics (Optional)**

You can add Google Analytics or other tracking:

1. Get tracking code
2. Add to HTML template in workflow
3. Monitor documentation usage

## 🔒 **Security Considerations**

- Documentation is public (GitHub Pages limitation)
- Don't include sensitive information
- Test reports show only public test data
- Repository must be public for free GitHub Pages

## 🎉 **Next Steps**

After setup:

1. **Push changes** to trigger first deployment
2. **Wait 5-10 minutes** for site to be available
3. **Visit your documentation site** at the URL above
4. **Share the link** with your team and stakeholders
5. **Start development** using the TDD guide

---

**Ready to enable GitHub Pages?** Follow Step 1 above and your documentation will be live in minutes! 🚀
