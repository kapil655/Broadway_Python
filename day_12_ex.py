def enroll_course(*args, **kwargs):
    length = len(args)

    if length == 0:
        return f'{kwargs.get("name")} {kwargs.get("level", "beginner")} have {length} subject enrolled'
    else:
        return f'{kwargs.get("name")} {kwargs.get("level", "beginner")} have {length} subjects enrolled'


print(
    enroll_course(
        "python",
        "django",
        "SQL",
        name="kamala",
        level="pro"
    )
)