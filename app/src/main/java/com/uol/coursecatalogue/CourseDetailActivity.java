package com.uol.coursecatalogue;

import android.content.ActivityNotFoundException;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

public class CourseDetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_course_detail);

        if (getSupportActionBar() != null) {
            getSupportActionBar().setDisplayHomeAsUpEnabled(true);
        }

        TextView tvDetailTitle = findViewById(R.id.tvDetailTitle);
        TextView tvDetailInstructor = findViewById(R.id.tvDetailInstructor);
        TextView tvDetailCredits = findViewById(R.id.tvDetailCredits);
        TextView tvDetailDescription = findViewById(R.id.tvDetailDescription);
        Button btnEmail = findViewById(R.id.btnEmail);

        // Read the values sent by MainActivity
        Intent intent = getIntent();
        String code = intent.getStringExtra(MainActivity.EXTRA_CODE);
        String title = intent.getStringExtra(MainActivity.EXTRA_TITLE);
        String instructor = intent.getStringExtra(MainActivity.EXTRA_INSTRUCTOR);
        final String email = intent.getStringExtra(MainActivity.EXTRA_EMAIL);
        String description = intent.getStringExtra(MainActivity.EXTRA_DESCRIPTION);
        int creditHours = intent.getIntExtra(MainActivity.EXTRA_CREDIT_HOURS, 0);

        // Screen title is the course code
        setTitle(code);

        tvDetailTitle.setText(title);
        tvDetailInstructor.setText("Instructor: " + instructor);
        tvDetailCredits.setText("Credit Hours: " + creditHours);
        tvDetailDescription.setText(description);

        // Email only this course's instructor
        btnEmail.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent emailIntent = new Intent(Intent.ACTION_SENDTO, Uri.parse("mailto:" + email));
                try {
                    startActivity(emailIntent);
                } catch (ActivityNotFoundException e) {
                    Toast.makeText(CourseDetailActivity.this, "No email app found", Toast.LENGTH_SHORT).show();
                }
            }
        });
    }

    @Override
    public boolean onSupportNavigateUp() {
        finish();
        return true;
    }
}
