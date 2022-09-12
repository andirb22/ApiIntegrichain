import {Injectable} from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

import { Book } from '../models/book.model';


const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable()
export class BookService {

  constructor(private http:HttpClient) {}

  private bookUrl = 'http://localhost:4000/books';

  public getBooks() {
    console.log(this.bookUrl)
    return this.http.get<Book[]>(this.bookUrl );
  }

  public getBook(id) {
    return this.http.get(this.bookUrl + "/"+ id);
  }

  public deleteBook(book) {
    return this.http.delete(this.bookUrl + "/"+ book.id);
  }

  public createBook(book) {
    console.log(book);
    return this.http.post<Book>(this.bookUrl , book);
    /*
    ngOnInit() {          
      this.http.post<Article>('https://reqres.in/api/posts', { title: 'Angular POST Request Example' }).subscribe(data => {
          this.postId = data.id;
      })
      */
  
  }

  public updateBook(book) {
    return this.http.put<Book>(this.bookUrl + "/update-book", book);
  }

}
