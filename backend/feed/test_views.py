import unittest
from feed.views import ChaptersListView, CategoryByChapterListView, CategoriesListView, SubcategoryByCategoryListView, SubcategoriesListView, ServicesBySubcategoryListView, ServicesListCreateView, ServicesRetrieveUpdateDestroyView, OrdersBySubcategoryListView, OrdedersListCreateView, OrdersRetriveUpdateDestroyView
from feed.models import Category, Subcategory, Chapter, Service, Order
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class ChaptersListViewTests(APITestCase):

    def test_get_all_chapters(self):
        """
        Ensure we can get all chapters objects.
        """
        url = reverse('chapter-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class CategoryByChapterListViewTests(APITestCase):
    
    def test_get_categories_by_chapter(self):
        """
        Ensure we can get categories filtered by chapter.
        """
        chapter = Chapter.objects.create(name='Test Chapter')
        category = Category.objects.create(name='Test Category', chapter=chapter)
        
        url = reverse('category-by-chapter-list', kwargs={'chapter_id': chapter.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], category.name)
        
class CategoriesListViewTests(APITestCase):

    def test_get_all_categories(self):
        """
        Ensure we can get all categories objects.
        """
        url = reverse('category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class SubcategoryByCategoryListViewTests(APITestCase):

    def test_get_subcategories_by_category(self):
        """
        Ensure we can get subcategories filtered by category.
        """
        category = Category.objects.create(name='Test Category')
        subcategory = Subcategory.objects.create(name='Test Subcategory', category=category)
        
        url = reverse('subcategory-by-category-list', kwargs={'category_id': category.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], subcategory.name)
        
class SubcategoriesListViewTests(APITestCase):

    def test_get_all_subcategories(self):
        """
        Ensure we can get all subcategories objects.
        """
        url = reverse('subcategory-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
class ServicesBySubcategoryListViewTests(APITestCase):

    def test_get_services_by_subcategory(self):
        """
        Ensure we can get services filtered by subcategory.
        """
        subcategory = Subcategory.objects.create(name='Test Subcategory')
        service = Service.objects.create(name='Test Service', subcategory=subcategory)
        
        url = reverse('service-by-subcategory-list', kwargs={'subcategory_id': subcategory.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], service.name)
        
class ServicesListCreateViewTests(APITestCase):

    def test_create_service(self):
        """
        Ensure we can create a new service object.
        """
        data = {'name': 'Test Service'}
        url = reverse('service-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Service.objects.count(), 1)
        self.assertEqual(Service.objects.get().name, 'Test Service')

    def test_get_all_services(self):
        """