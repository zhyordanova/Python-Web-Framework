
# **Lab: Class-Based-Views Deep Dive**
# **Basic News App using CBV's**
*We will create a **simple news app**. We will have **2 forms**: one for adding a new **Source** (a simple model with a **name** and an **url**) and one for adding an **Article** (it should have **title**, **image**, **description** and an existing **source instance**). All the articles will be displayed on the **Home page**. We will practice **handling forms** and using **mixins** with **CBV's**.*
1. ## **Setup a new project**
Create a **new project** in a separate folder. Create a **single app** in the project folder. Make the **needed configurations**
1. ## **Models**
### **Source**
- **name** – character field with max length of 50
- **url** – url field with max length of 200
### **Article**
- **title** – character field with max length of 100
- **description** – text field
- **imageUrl** – url field with max length of 200
- **source** – foreign key
1. ## **Template separation**
Take the provided **resources** (**html** and **css**) and separate the html into proper **templates**
1. ## **Forms**
Create **form classes** for your models. Add the needed **widgets** to apply the **styles** provided.
1. ## **Pages**
Use the needed types of **class-based-views** for each of the pages
### **Home page**
![Aspose Words 9b75d108-2b97-460b-8a8b-a95e50193176 001](https://user-images.githubusercontent.com/66780885/127976544-edab5c06-d520-45c7-9392-ead0757e0694.png)

The home page should display **all articles** as shown in the picture above
### **Source Create page**
![Aspose Words 9b75d108-2b97-460b-8a8b-a95e50193176 002](https://user-images.githubusercontent.com/66780885/127976644-e400b23b-c70d-4b0f-86da-382c9f90bd1c.png)

The source create page should display a **form** for **creating a source**.
### **Article Create page**
![Aspose Words 9b75d108-2b97-460b-8a8b-a95e50193176 003](https://user-images.githubusercontent.com/66780885/127976726-ffcfd982-cdfb-4c43-830f-0a1361d9b766.png)

The article create page should display a **form** for **creating an article**.
### **Sources page**
![Aspose Words 9b75d108-2b97-460b-8a8b-a95e50193176 004](https://user-images.githubusercontent.com/66780885/127976806-be6a8270-5299-4cb9-a09c-34e8925cf177.png)

The sources page should display **all sources** as shown in the picture above. Upon **clicking** on **"See related articles"**, a **source details page** should be displayed. When clicking the **link** of the source, open its **url** in a **new tab**
### **Source Details page**
![Aspose Words 9b75d108-2b97-460b-8a8b-a95e50193176 005](https://user-images.githubusercontent.com/66780885/127976916-87102696-5ac0-4bce-99ce-671c8478f746.png)

The source details page should display information as shown in the picture above.

***HINT: Use SingleObjectMixin with ListView – might want to read*** [this](https://docs.djangoproject.com/en/3.1/topics/class-based-views/mixins/#using-singleobjectmixin-with-listview)

Follow us:

![Aspose Words 9b75d108-2b97-460b-8a8b-a95e50193176 007](https://user-images.githubusercontent.com/66780885/127977079-87ebf28d-4003-48c3-aab9-905c60297d49.png)
