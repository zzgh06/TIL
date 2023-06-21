# level 과 exp 구현

## 1. accounts/models.py
```python
class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=30)
    joined_at = models.DateTimeField(auto_now_add=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    level = models.IntegerField(default=1)
    profile_image = ProcessedImageField(blank=True,
                                        upload_to='users',
                                        processors=[ResizeToFill(200, 200)],
                                        format='JPEG',
                                        options={'quality': 70})
    
    def image_path(instance, filename):
        return f'account/{instance.pk}/{filename}'
    
    def liked_groups(self):
        return Group.objects.filter(like_users=self)
```

    1. level를 구현하기 위해 accounts/models.py User 클래스에 level 필드 값 추가

## 2. accounts/views.py

```python
@login_required
def profile(request, username):
    User = get_user_model()
    person = User.objects.get(username=username)
    post_comments = person.postcomment_set.count()
    groups = person.group_set.all().order_by('-created_at')
    group_comments = person.groupcomment_set.count()

    liked_groups = person.liked_groups()
    liked_posts = person.like_posts.all()

    score = groups.count() * 50 + post_comments * 5 + group_comments * 5

    if score < 200:
        level = 1
        min_score = 0
        max_score = 200
        need_score = 200
    elif score < 400:
        level = 2
        min_score = 200
        max_score = 400
        need_score = 200
    elif score < 600:
        level = 3
        min_score = 400
        max_score = 600
        need_score = 200
    elif score < 800:
        level = 4
        min_score = 600
        max_score = 800
        need_score = 200
    elif score >= 1000:
        level = 5
        min_score = 800
        max_score = 'MAX'
        need_score = 200

    if max_score == 'MAX':
        expbar = 100
        restexp = 0
    else:
        now_score = score - min_score
        expbar = (now_score / need_score) * 100
        restexp = need_score - now_score

    if person.level != level:
        person.level = level
        person.save()

    level_dict = {1: '뉴비', 2: '초보', 3: '중수', 4: '고수', 5: '마스터'}

    context = {
        'person': person,
        'groups': groups, 
        'level_name': level_dict[level],
        'max_score': max_score,
        'liked_posts': liked_posts,
        'liked_groups' : liked_groups,
        'score': score,
        'expbar': expbar,
        'restexp': restexp,
    }
    return render(request, 'accounts/profile.html', context)

```
    1. profile 뷰함수에 점수를 부여할 기준선정
      1) 포스트 댓글 :  post_comments = person.postcomment_set.count()
      2) 그룹 생성 : groups = person.group_set.all().order_by('-created_at')
      3) 그룹 댓글group_comments = person.groupcomment_set.count()

    2. 점수 계산
    그룹의 개수에 50을 곱하고, 게시글 댓글 수와 그룹 댓글 수에 각각 5를 곱하여 더한다.
  
      score = groups.count() * 50 + post_comments * 5 + group_comments * 5

    3. 레벨 기준(1~5)
    계산된 점수를 기준으로 사용자의 레벨을 결정
    if score < 200:
        level = 1
        min_score = 0
        max_score = 200
        need_score = 200
    (생략...)
    elif score >= 1000:
        level = 5
        min_score = 800
        max_score = 'MAX'
        need_score = 200

    4. expbar 기준
    최대 점수가 'MAX'인 경우, 경험치 바(expbar)는 100으로, 남은 경험치(restexp)는 0으로 설정
    그렇지 않은 경우, 현재 점수를 최소 점수에서 뺀 값과 필요한 점수를 비교하여 경험치 바와 남은 경험치를 계산
    if max_score == 'MAX':
        expbar = 100
        restexp = 0
    else:
        now_score = score - min_score
        expbar = (now_score / need_score) * 100
        restexp = need_score - now_score

    5. 사용자의 레벨이 변경되었다면, 데이터베이스에 저장
    if person.level != level:
        person.level = level
        person.save()
        
    6. 각 레벨에 따른 이름을 딕셔너리(level_dict)에 정의하여 context에 추가
    level_dict = {1: '뉴비', 2: '초보', 3: '중수', 4: '고수', 5: '마스터'}

    
