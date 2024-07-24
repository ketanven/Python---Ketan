# manage_institute/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student,Teacher,Club,Book
from django.utils import timezone

def home(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_clubs = Club.objects.count()
    total_books = Book.objects.count()

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_clubs': total_clubs,
        'total_books': total_books,
    }
    return render(request, 'index.html', context)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def create(request):
    if request.method == "POST":
        try:
            student = Student.objects.get(full_name=request.POST['full_name'], date_of_birth=request.POST['date_of_birth'])
            msg = "Student with this name and date of birth already exists!"
            return render(request, 'create.html', {'msg': msg})
        except Student.DoesNotExist:
            try:
                date_of_joining = timezone.datetime.strptime(request.POST['date_of_joining'], '%Y-%m-%dT%H:%M')
            except ValueError:
                msg = "Invalid date format for Date of Joining!"
                return render(request, 'create.html', {'msg': msg})

            Student.objects.create(
                full_name=request.POST['full_name'],
                date_of_birth=request.POST['date_of_birth'],
                date_of_joining=date_of_joining,
                address=request.POST['address']
            )
            return redirect('student_list')
    else:
        return render(request, 'create.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.full_name = request.POST['full_name']
        student.date_of_birth = request.POST['date_of_birth']
        student.date_of_joining = timezone.datetime.strptime(request.POST['date_of_joining'], '%Y-%m-%dT%H:%M')
        student.address = request.POST['address']
        student.save()
        return redirect('student_list')
    return render(request, 'edit_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'delete_student.html', {'student': student})



# _________________________________________________________________________________________

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def create_teacher(request):
    if request.method == "POST":
        try:
            teacher = Teacher.objects.get(full_name=request.POST['full_name'], date_of_birth=request.POST['date_of_birth'])
            msg = "Teacher with this name and date of birth already exists!"
            return render(request, 'create_teacher.html', {'msg': msg})
        except Teacher.DoesNotExist:
            try:
                date_of_joining = timezone.datetime.strptime(request.POST['date_of_joining'], '%Y-%m-%dT%H:%M')
            except ValueError:
                msg = "Invalid date format for Date of Joining!"
                return render(request, 'create_teacher.html', {'msg': msg})

            Teacher.objects.create(
                full_name=request.POST['full_name'],
                date_of_birth=request.POST['date_of_birth'],
                date_of_joining=date_of_joining,
                address=request.POST['address'],
                compensation=request.POST['compensation']
            )
            return redirect('teacher_list')
    else:
        return render(request, 'create_teacher.html')

def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.full_name = request.POST['full_name']
        teacher.date_of_birth = request.POST['date_of_birth']
        teacher.date_of_joining = timezone.datetime.strptime(request.POST['date_of_joining'], '%Y-%m-%dT%H:%M')
        teacher.address = request.POST['address']
        teacher.compensation = request.POST['compensation']
        teacher.save()
        return redirect('teacher_list')
    return render(request, 'edit_teacher.html', {'teacher': teacher})

def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'delete_teacher.html', {'teacher': teacher})


# _____________________________________________________________________


def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'club_list.html', {'clubs': clubs})

def create_club(request):
    if request.method == "POST":
        # Check if the club already exists
        try:
            club = Club.objects.get(name=request.POST['name'], founded_date=request.POST['founded_date'])
            msg = "Club with this name and founded date already exists!"
            return render(request, 'create_club.html', {'msg': msg})
        except Club.DoesNotExist:
            # Parse the date from the input format
            try:
                founded_date = timezone.datetime.strptime(request.POST['founded_date'], '%Y-%m-%d').date()
            except ValueError:
                msg = "Invalid date format for Founded Date!"
                return render(request, 'create_club.html', {'msg': msg})

            # Create the new club
            Club.objects.create(
                name=request.POST['name'],
                description=request.POST['description'],
                founded_date=founded_date,
                president=request.POST['president'],
                members_count=int(request.POST['members_count'])
            )
            return redirect('club_list')
    else:
        return render(request, 'create_club.html')

def edit_club(request, id):
    club = get_object_or_404(Club, id=id)
    if request.method == 'POST':
        # Update the club details
        club.name = request.POST['name']
        club.description = request.POST['description']
        club.founded_date = timezone.datetime.strptime(request.POST['founded_date'], '%Y-%m-%d').date()
        club.president = request.POST['president']
        club.members_count = int(request.POST['members_count'])
        club.save()
        return redirect('club_list')
    return render(request, 'edit_club.html', {'club': club})

def delete_club(request, id):
    club = get_object_or_404(Club, id=id)
    if request.method == 'POST':
        club.delete()
        return redirect('club_list')
    return render(request, 'delete_club.html', {'club': club})


#___________________________________________________________________________


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def create_book(request):
    if request.method == "POST":
        # Check if the book already exists
        if Book.objects.filter(isbn=request.POST['isbn']).exists():
            msg = "Book with this ISBN already exists!"
            return render(request, 'create_book.html', {'msg': msg})
        
        # Create the new book
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            published_date=request.POST['published_date'],
            isbn=request.POST['isbn'],
            pages=int(request.POST['pages']),
            language=request.POST['language']
        )
        return redirect('book_list')
    else:
        return render(request, 'create_book.html')

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        # Update the book details
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.published_date = timezone.datetime.strptime(request.POST['published_date'], '%Y-%m-%d').date()
        book.isbn = request.POST['isbn']
        book.pages = int(request.POST['pages'])
        book.language = request.POST['language']
        book.save()
        return redirect('book_list')
    return render(request, 'edit_book.html', {'book': book})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'delete_book.html', {'book': book})


from .models import User


def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')

        # Check if password and confirm password match
        if password != cpassword:
            msg = "Password and Confirm Password don't match!"
            return render(request, 'register.html', {'msg': msg})

        # Create new user
        new_user = User.objects.create(
            name=request.POST.get('name'),
            email=email,
            mobile=request.POST.get('mobile'),
            password=password,
            profile=request.FILES.get('profile'),
            institute=request.POST.get('institute')
        )

        # Redirect to login page with success message
        msg = "Registration successfully completed!"
        return render(request, 'login.html', {'msg': msg})

    else:
        return render(request, 'register.html')




    
    




def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email=request.POST['email'])
            
            if user.password == request.POST['password']:
                request.session['email'] = user.email
                request.session['profile'] = user.profile.url
                request.session['name'] = user.name
                
                return redirect('home')

            else:
                msg = "Password doesn't match !!"
                return render(request, 'login.html', {'msg': msg})
        except User.DoesNotExist:
            msg = "Email doesn't match !!"
            return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')


def logout(request):
    del request.session['email']
    del request.session['profile']

    return redirect("login")



def fpass(request):
    if request.method == "POST":
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(email=email)

            if user.password == old_password:
                user.password = new_password
                user.save()
                msg = "Password updated successfully!"
            else:
                msg = "Old password is incorrect!"

            return redirect('home')
        except User.DoesNotExist:
            msg = "Email not found!"
            return render(request, 'forgot_password.html', {'msg': msg})

    else:
        return render(request, 'forgot_password.html')




from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(user_email):
    subject = 'Welcome to Our Site'
    message = 'Thank you for registering on our site.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    send_mail(subject, message, email_from, recipient_list)



from django.shortcuts import render, redirect
from .models import User  # Ensure this is imported from the correct location

def profilepage(request):
    user = User.objects.get(email=request.session.get('email'))
    
    if request.method == "POST":
        # Update user details
        user.name = request.POST.get('name', user.name)
        user.email = request.POST.get('email', user.email)
        user.mobile = request.POST.get('mobile', user.mobile)
        user.institute = request.POST.get('institute', user.institute)
        
        if 'profile' in request.FILES:
            try:
                user.profile = request.FILES['profile']
                user.save()
                request.session['profile'] = user.profile.url
            except Exception as e:
                # Handle specific exceptions if necessary, or provide a generic error message
                return render(request, 'profile.html', {'user': user, 'error': 'Error uploading file. Please try again.'})
        
        try:
            user.save()
            return redirect('home')  # Redirect to home page on successful update
        except Exception as e:
            return render(request, 'profile.html', {'user': user, 'error': 'Error saving user details. Please try again.'})
    
    return render(request, 'profile.html', {'user': user})


        
       
    