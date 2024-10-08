# Дополнительное практическое задание по модулю: "Классы и объекты."
# Задание "Свой YouTube":

import time

class User:
    def __init__ (self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'User(nickname={self.nickname}, password={self.password}, age={self.age})'

    def __eq__(self, other):
        return isinstance(other, User) and self.nickname == other.nickname


class Video:
    def __init__ (self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Video(title={self.title}, duration={self.duration}, adult_mode={self.adult_mode})'


class UrTube:
    def __init__ (self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in (self, nickname, password):
        hashed = hash(password)
        for user in self.users:
            if nickname == user.nickname and hashed == user.password:
                self.current_user = user.nickname
                return
            else:
                print('Неправильно введены имя или пароль')
                return

    def register (self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = nickname
        self.current_user_age = age

    def log_out (self):
        self.current_user = None

    def add (self, *videos):
        for video in videos:
            if all(v.title != video.title for v in self.videos):
                self.videos.append(video)
            else:
                print(f"Видео с названием '{video.title}' уже существует")

    def get_videos (self, word):
        return [video.title for video in self.videos if word.lower() in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user_age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                while video.time_now < video.duration:
                    print(video.time_now + 1, end=' ')
                    video.time_now += 1
                    time.sleep(1)
                video.time_now = 0
                print("Конец видео")
                return
        print("Видео не найдено")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
