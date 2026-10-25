package com.uol.coursecatalogue;

import android.content.Intent;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity implements CourseAdapter.OnItemClickListener {

    // Keys for the extras sent to CourseDetailActivity
    public static final String EXTRA_CODE = "com.uol.coursecatalogue.CODE";
    public static final String EXTRA_TITLE = "com.uol.coursecatalogue.TITLE";
    public static final String EXTRA_INSTRUCTOR = "com.uol.coursecatalogue.INSTRUCTOR";
    public static final String EXTRA_EMAIL = "com.uol.coursecatalogue.EMAIL";
    public static final String EXTRA_DESCRIPTION = "com.uol.coursecatalogue.DESCRIPTION";
    public static final String EXTRA_CREDIT_HOURS = "com.uol.coursecatalogue.CREDIT_HOURS";

    private RecyclerView rvCourses;
    private ArrayList<Course> courses;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        rvCourses = findViewById(R.id.rvCourses);

        courses = new ArrayList<>();
        courses.add(new Course("SE-1101", "Programming Fundamentals", "Dr. Ahmed Raza", "ahmed.raza@se.uol.edu.pk",
                "Covers the basics of programming in C++: variables, data types, conditions, loops, functions and arrays, with weekly lab problems.", 4));
        courses.add(new Course("SE-1201", "Object Oriented Programming", "Ms. Ayesha Khan", "ayesha.khan@se.uol.edu.pk",
                "Introduces classes, objects, encapsulation, inheritance, polymorphism and abstraction, and how to design programs around objects.", 4));
        courses.add(new Course("SE-2101", "Data Structures and Algorithms", "Dr. Usman Tariq", "usman.tariq@se.uol.edu.pk",
                "Studies arrays, linked lists, stacks, queues, trees, graphs and hashing, along with sorting and searching algorithms and their complexity.", 4));
        courses.add(new Course("SE-2203", "Software Requirements Engineering", "Ms. Sana Iqbal", "sana.iqbal@se.uol.edu.pk",
                "Teaches how to elicit, analyse, document and validate software requirements, including use cases and requirement specifications.", 3));
        courses.add(new Course("SE-2301", "Database Systems", "Mr. Bilal Hassan", "bilal.hassan@se.uol.edu.pk",
                "Covers relational database design, ER modelling, normalization, SQL queries and transactions, with hands-on database labs.", 4));
        courses.add(new Course("SE-3102", "Software Design and Architecture", "Dr. Hina Malik", "hina.malik@se.uol.edu.pk",
                "Explores design principles, UML, design patterns and architectural styles used to build maintainable software systems.", 3));
        courses.add(new Course("SE-3205", "Operating Systems", "Mr. Kamran Ali", "kamran.ali@se.uol.edu.pk",
                "Explains processes, threads, CPU scheduling, synchronization, deadlocks, memory management and file systems.", 3));
        courses.add(new Course("SE-3301", "Software Quality Engineering", "Ms. Nida Farooq", "nida.farooq@se.uol.edu.pk",
                "Focuses on software testing techniques, quality assurance, test planning and quality metrics across the development lifecycle.", 3));
        courses.add(new Course("SE-4101", "Mobile Application Development", "Mr. Faisal Mehmood", "faisal.mehmood@se.uol.edu.pk",
                "Teaches Android app development in Java with Android Studio: activities, intents, layouts, RecyclerView and data storage.", 3));
        courses.add(new Course("SE-4203", "Information Security", "Dr. Zainab Shah", "zainab.shah@se.uol.edu.pk",
                "Covers security principles, cryptography, authentication, network security and common attacks and how to defend against them.", 3));

        rvCourses.setLayoutManager(new LinearLayoutManager(this));
        rvCourses.setAdapter(new CourseAdapter(courses, this));
    }

    @Override
    public void onItemClick(int position) {
        Course course = courses.get(position);

        Intent intent = new Intent(MainActivity.this, CourseDetailActivity.class);
        intent.putExtra(EXTRA_CODE, course.getCode());
        intent.putExtra(EXTRA_TITLE, course.getTitle());
        intent.putExtra(EXTRA_INSTRUCTOR, course.getInstructor());
        intent.putExtra(EXTRA_EMAIL, course.getEmail());
        intent.putExtra(EXTRA_DESCRIPTION, course.getDescription());
        intent.putExtra(EXTRA_CREDIT_HOURS, course.getCreditHours());
        startActivity(intent);
    }
}
