package com.books.books;

import java.util.concurrent.atomic.AtomicLong;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller // This means that this class is a Controller
@RequestMapping(path = "/books")
@CrossOrigin(origins = "*")
public class BookController {
	public final AtomicLong id = new AtomicLong(1);
	@Autowired
	private BookRepository bookRepository;

	@GetMapping(path = "/all")
	public @ResponseBody Iterable<Book> getAllUsers() {
		// This returns a JSON or XML with the users
		return bookRepository.findAll();
	}
	
	@PostMapping(path="/add") 
	  public @ResponseBody String addNewUser (@RequestParam String title
	      , @RequestParam String author, @RequestParam String genre, @RequestParam String year) {
		
		Book b = new Book();
		b.setAuthor(author);
		b.setGenre(genre);
		b.setTitle(title);
		b.setYear(year);
		bookRepository.save(b);
	    return "Saved";
	  }
	
	@PostMapping(path="/delete") 
	  public @ResponseBody String deleteByID (@RequestParam String id) {
		
		bookRepository.deleteById(Integer.parseInt(id));
	    return "Deleted";
	  }
}
