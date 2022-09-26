import { Component } from '@angular/core';
import {  Router } from '@angular/router';
import {Book} from 'src/app/models/book.model';
import { BookService } from 'src/app/services/book.service';
import {MatDialog} from '@angular/material/dialog';



@Component({
  selector: 'app-add-tutorial',
  templateUrl: './add-book.component.html',
  styleUrls: ['./add-book.component.css']
})

export class AddBookComponent {

  book: Book = {
    title: '',
    author: '',
    read: false
  };
  submitted = false;

  constructor(private bookService: BookService,private router: Router) { }


  saveBook(): void {
    const data = {
      "title": this.book.title,
      "author": this.book.author,
      "read": 0
    };

    this.bookService.create(data)
      .subscribe({
        next: (res) => {
          console.log(res);
          this.submitted = true;
          this.router.navigate(['/books']);
        },
        error: (e) => console.error(e)
      });
  }

  newBook(): void {
    this.submitted = false;
    this.book = {
      title: '',
      author: '',
      read: false
    };
  }

}