from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from .views import MainView, RegistrationView, LoginUserView, LogoutView, ProfileView, ProfileUpdateView, \
    UserPasswordChangeView, UserProfileDetailView

app_name = 'main_app'


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('registration/', RegistrationView.as_view(), name='registration'),

    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginUserView.as_view(), name='login'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('user-profile/<int:pk>/', UserProfileDetailView.as_view(), name='profile_detail'),
    path('update/', ProfileUpdateView.as_view(), name='update'),

    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='profile/password_change_done.html'), name='password_change_done'),

    path('password_reset/', PasswordResetView.as_view(template_name='profile/password_reset_form.html',
                                                       email_template_name='profile/password_reset_email.html',
                                                       success_url=reverse_lazy('main_app:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='profile/password_reset_done.html'), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='profile/password_reset_confirm.html',
                                                                                success_url=reverse_lazy('main_app:password_reset_complete')), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name='profile/password_reset_complete.html'), name='password_reset_complete'),




]