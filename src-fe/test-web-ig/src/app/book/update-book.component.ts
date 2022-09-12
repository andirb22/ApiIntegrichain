import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

import { Book } from '../models/book.model';
import { BookService } from './book.service';

@Component({
  selector: 'app-book-update',
  templateUrl: './update-book.component.html',
})
export class UpdateBookComponent implements OnInit {

  book: any = {};

  constructor(private router: Router, private route: ActivatedRoute, private bookService: BookService) {
    
  }

  ngOnInit() {
    this.bookService.getBook(this.route.snapshot.params['id'])
      .subscribe(data => {
        this.book = data;
      });
  };

  updateBook(): void {
    this.bookService.updateBook(this.book)
      .subscribe(data => {
        alert("Book updated successfully.");
        this.router.navigate(['/books']);
      });

  };

}