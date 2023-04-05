import cv2
import numpy as np
import os
import sqlite3
import datetime

def take_attendance():
    conn = sqlite3.connect('main.db')
    c = conn.cursor()
    
    c.execute("SELECT id, name FROM subjects")
    subjects = c.fetchall()
    
    c.execute("SELECT * FROM students")
    students = c.fetchall()
    
    subject_names = [subject[1] for subject in subjects]
    subject_ids = [subject[0] for subject in subjects]
    
    present_students = []
    for i in range(len(subject_names)):
        present_students.append([])

