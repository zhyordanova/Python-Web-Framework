
# **Lab: Django REST Framework**
# **Books API**
Create a simple **Books API** using the **Django REST framework**.
1. ## **Create the Project**
- **Create** your **project** and your **API app**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 001](https://user-images.githubusercontent.com/66780885/128044785-44b0c871-803e-4369-bb5b-0035807e3f2b.png)

2. ## **Setup**
- Make sure that you have **djangorestframework** installed (if not, install it using pip)
- Add **'rest\_framework'** to the **INSTALLED\_APPS**
- Add **'books\_api'** to the **INSTALLED\_APPS**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 002](https://user-images.githubusercontent.com/66780885/128044929-fea11bdc-4a97-41c1-9ed4-6a6efac77b80.png)

- **Configure** and **create** your **database**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 003](https://user-images.githubusercontent.com/66780885/128045065-8089d48c-4e07-4171-8e1d-752cd03ef2de.png)

3. ## **Create you Model**
Create the **Book model** as shown below

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 004](https://user-images.githubusercontent.com/66780885/128045209-8ae4037d-b888-4ba4-9c57-daf08e72a824.png)

Make **migrations** and **register the model** in the **admin.py** file

4. ## **Create the Serializer**
Create a new file called **'serializers.py'** and create the **BookSerializer**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 005](https://user-images.githubusercontent.com/66780885/128045323-ffe8eaf1-0d44-4ee3-9d22-39acf89200e2.png)

5. ## **Creating the Views**
First, create the **ListBookView**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 006](https://user-images.githubusercontent.com/66780885/128045470-df231c8d-dc3e-4075-a924-6367cb9a2539.png)

And then, the **DetailBookView**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 007](https://user-images.githubusercontent.com/66780885/128045595-7ca03e2a-8207-4aba-8633-2a96ffd6f81c.png)

6. ## **Configure the urls.py Files**
Create **urls.py** file in the **app**, and add the **urls**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 008](https://user-images.githubusercontent.com/66780885/128045787-172eb7cd-7ab7-46f5-9ba2-b9e83bafbd49.png)

And the **urls.py** file in the **project**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 009](https://user-images.githubusercontent.com/66780885/128045850-f1b9bd39-1bf1-4c20-b6d8-4208730b7ac8.png)

7. ## **Create a superuser**
Create a **superuser** and **create some books**

8. ## **Test The API**

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 010](https://user-images.githubusercontent.com/66780885/128045999-5e8c2033-9e46-48d4-aa72-7c3aec10a890.png)

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 011](https://user-images.githubusercontent.com/66780885/128046052-e1c1fe78-3a47-43af-92a1-dd36e253e96d.png)
Follow us:

![Aspose Words 35d5d42e-f949-4779-94ea-7db718836605 013](https://user-images.githubusercontent.com/66780885/128046237-34311d2c-29ca-411d-aea9-6a6873213dda.png)
