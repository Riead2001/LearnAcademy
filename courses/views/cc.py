from django.shortcuts import render, redirect
from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib import messages
from courses.models import course, UserCourse, Course, user_course,Scholarship


from django.shortcuts import render, redirect
from courses.models import Course, Tag, Learning, Video

def Cc(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        slug = request.POST.get('slug')
        description = request.POST.get('description')
        price = request.POST.get('price')
        discount = request.POST.get('discount', 0)
        length = request.POST.get('length')
        image = request.FILES.get('image')
        resource = request.FILES.get('resource')
        
        # Create the course object
        course = Course.objects.create(
            name=name,
            slug=slug,
            description=description,
            price=price,
            discount=discount,
            length=length,
            image=image,
            resource=resource
        )

        # Create Tags
        tag_descs = request.POST.getlist('tags')
        for tag_desc in tag_descs:
            Tag.objects.create(course=course, desc=tag_desc)

        # Create Learnings
        learning_descs = request.POST.getlist('learnings')
        for learning_desc in learning_descs:
            Learning.objects.create(course=course, desc=learning_desc)

        # Create Videos
        videos_data = request.POST.getlist('videos')
        for video_data in videos_data:
            # Split the video_data string and handle potential errors
            try:
                video_number, video_title, video_id, is_preview = video_data.split(',')
            except ValueError:
                # If the format is incorrect, skip this video_data
                continue

            # Create the Video object
            Video.objects.create(
                course=course,
                serial_number=video_number,
                title=video_title,
                video_id=video_id,
                is_preview=is_preview
            )

        # Redirect to home page after successful creation
        return redirect('home')

    return render(request, 'courses/cc.html')
