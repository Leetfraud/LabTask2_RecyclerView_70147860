# Mobile Application Development (CS02310) — Lab Task No. 02
## UOL Course Catalogue — RecyclerView List App
**The University of Lahore | Faculty of Information Technology | Department of Software Engineering**

---

### Student Information
- **Student Name**: Faseeh Ur Rehman
- **SAP ID**: 70147860
- **Course**: Mobile Application Development (CS02310)
- **Programme**: BS Software Engineering (7th Semester)
- **Section**: Section S
- **Task**: Lab Task No. 02 — RecyclerView List App
- **Mapped CLO**: CLO-4 (Bloom's: Creating / C6 → PLO-5 / GA-5)
- **GitHub Profile**: [https://github.com/Leetfraud](https://github.com/Leetfraud)
- **GitHub Repository**: [https://github.com/Leetfraud/LabTask2_RecyclerView_70147860](https://github.com/Leetfraud/LabTask2_RecyclerView_70147860)

---

### Project Overview
**UOL Course Catalogue** lets a BS-SE student browse the programme's courses and open the details of any one course. It is built in two linked scenarios:

1. **Scenario 1 — The Course List (`MainActivity`)**
   - `Course` model class with private fields (`code`, `title`, `instructor`, `email`, `description`, `creditHours`), one constructor and a getter for each.
   - `item_course.xml` — a `CardView` (rounded corners + elevation) showing the course code, title and credit hours.
   - `CourseAdapter` — extends `RecyclerView.Adapter` with a static inner `ViewHolder` that finds its three TextViews once.
   - Ten BS-SE courses in an `ArrayList`, shown in `rvCourses` with a `LinearLayoutManager`.

2. **Scenario 2 — The Course Details Screen (`CourseDetailActivity`)**
   - `OnItemClickListener` interface inside the adapter; the ViewHolder reports `getBindingAdapterPosition()` and `MainActivity` implements it.
   - `onItemClick(position)` gets the course with `courses.get(position)` and opens `CourseDetailActivity` with an explicit Intent carrying only that course's data (`public static final` key constants).
   - The details screen reads the extras with `getStringExtra()` / `getIntExtra()`, shows the title, instructor, credit hours and description, and sets the screen title to the course code.
   - **Email Instructor** opens the email app with `ACTION_SENDTO` and `mailto:` + that instructor's email, inside try–catch with a Toast fallback.

**Flow of one tap:** tap a card → click listener in the ViewHolder → `onItemClick(position)` in MainActivity → `courses.get(position)` → Intent with that course's data → `CourseDetailActivity`

---

### Project Structure
```text
LabTask2_RecyclerView_70147860/
├── app/
│   ├── build.gradle
│   ├── proguard-rules.pro
│   └── src/main/
│       ├── AndroidManifest.xml
│       ├── java/com/uol/coursecatalogue/
│       │   ├── Course.java
│       │   ├── CourseAdapter.java
│       │   ├── CourseDetailActivity.java
│       │   └── MainActivity.java
│       └── res/
│           ├── drawable/uol_logo.xml
│           ├── layout/
│           │   ├── activity_main.xml
│           │   ├── activity_course_detail.xml
│           │   └── item_course.xml
│           ├── mipmap-anydpi-v26/
│           └── values/
├── gradle/wrapper/
├── screenshots/                 # App screenshots used in the report
├── generate_report_pdf.py       # Script that builds the report PDF
├── build.gradle
├── settings.gradle
└── README.md
```

---

### How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Leetfraud/LabTask2_RecyclerView_70147860.git
   ```
2. Open the folder in Android Studio and let Gradle sync.
3. Run the `app` configuration on an emulator or a connected device.
