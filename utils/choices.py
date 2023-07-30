from django.db.models import TextChoices


class UserRoleChoices(TextChoices):
    DIRECTOR = "director", "Директор"
    MANAGER = "manager", "Менеджер"
    SUPER_LIBRARIAN = "super_librarian", "Супер библиотекарь"
    LIBRARIAN = "librarian", "Библиотекарь"
    ACCOUNTING = "accounting", "Бухгалтерия"

    READER = "reader", "Читатель"


class AuthStatus(TextChoices):
    NEW = "new", "Новый"
    VERIFY = "verify", "На проверке"
    HALF_DONE = "half_done", "Частично заполнен"
    DONE = "done", "Заполнен"
