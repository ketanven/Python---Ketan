from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from .models import Product, ProductSubCategory

# Define a ModelForm for ProductSubCategory to simplify form handling
class ProductSubCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductSubCategory
        fields = ['product', 'price', 'image', 'model', 'ram']

def product_list(request):
    # Retrieve the search query from GET parameters
    search_query = request.GET.get('search', '')

    # Fetch all products
    products = Product.objects.all()
    
    # Filter subcategories based on the search query
    sub_categories = ProductSubCategory.objects.filter(product__product_name__icontains=search_query)
    
    # Initialize a blank form for creating new subcategories
    create_form = ProductSubCategoryForm()

    # Render the product list template with the context
    return render(request, 'products/product.html', {
        'products': products,
        'sub_categories': sub_categories,
        'create_form': create_form,
    })

def product_sub_category_create(request):
    # Handle form submission for creating a new subcategory
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Save the new subcategory
            return redirect('product_list')  # Redirect to the product list after saving

    # Redirect to the product list if not a POST request
    return redirect('product_list')

def product_sub_category_update(request, pk):
    # Retrieve the specific subcategory to update
    sub_category = get_object_or_404(ProductSubCategory, pk=pk)

    # Handle form submission for updating an existing subcategory
    if request.method == 'POST':
        form = ProductSubCategoryForm(request.POST, request.FILES, instance=sub_category)
        if form.is_valid():
            form.save()  # Save the updated subcategory
            return redirect('product_list')  # Redirect to the product list after saving
    else:
        # Initialize the form with the current subcategory data
        form = ProductSubCategoryForm(instance=sub_category)

    # Render the form template for updating the subcategory
    return render(request, 'products/product_sub_category_form.html', {'form': form})

def product_sub_category_delete(request, pk):
    # Retrieve the specific subcategory to delete
    sub_category = get_object_or_404(ProductSubCategory, pk=pk)

    # Handle form submission for deleting the subcategory
    if request.method == 'POST':
        sub_category.delete()  # Delete the subcategory
        return redirect('product_list')  # Redirect to the product list after deletion

    # Render the confirmation template for deletion
    return render(request, 'products/product_sub_category_confirm_delete.html', {'sub_category': sub_category})
