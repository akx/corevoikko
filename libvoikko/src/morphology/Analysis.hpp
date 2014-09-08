/* The contents of this file are subject to the Mozilla Public License Version 
 * 1.1 (the "License"); you may not use this file except in compliance with 
 * the License. You may obtain a copy of the License at 
 * http://www.mozilla.org/MPL/
 * 
 * Software distributed under the License is distributed on an "AS IS" basis,
 * WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
 * for the specific language governing rights and limitations under the
 * License.
 * 
 * The Original Code is Libvoikko: Library of natural language processing tools.
 * The Initial Developer of the Original Code is Harri Pitkänen <hatapitk@iki.fi>.
 * Portions created by the Initial Developer are Copyright (C) 2009
 * the Initial Developer. All Rights Reserved.
 * 
 * Alternatively, the contents of this file may be used under the terms of
 * either the GNU General Public License Version 2 or later (the "GPL"), or
 * the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
 * in which case the provisions of the GPL or the LGPL are applicable instead
 * of those above. If you wish to allow use of your version of this file only
 * under the terms of either the GPL or the LGPL, and not to allow others to
 * use your version of this file under the terms of the MPL, indicate your
 * decision by deleting the provisions above and replace them with the notice
 * and other provisions required by the GPL or the LGPL. If you do not delete
 * the provisions above, a recipient may use your version of this file under
 * the terms of any one of the MPL, the GPL or the LGPL.
 *********************************************************************************/

#ifndef VOIKKO_MORPHOLOGY_ANALYSIS
#define VOIKKO_MORPHOLOGY_ANALYSIS

#include <string>
#include <map>

namespace libvoikko { namespace morphology {

/**
 * Results from morphological analysis. See
 * doc/morphological-analysis.txt for more information about the
 * attributes that should be included in the analysis.
 */
class Analysis {
	public:
		Analysis();
		~Analysis();
		
		/**
		 * Adds an attribute to analysis. Ownership of value
		 * is transferred to this object.
		 */
		void addAttribute(const char * key, wchar_t * value);
		
		/**
		 * Deletes an attribute from analysis.
		 */
		void removeAttribute(const char * key);
		
		/**
		 * Returns a null terminated array of strings containing
		 * the attribute names in this analysis.
		 */
		const char ** getKeys() const;

		/**
		 * Returns the value of given attribute. If no such
		 * attribute exists, returns null.
		 */
		const wchar_t * getValue(const char * key) const;
	private:
		Analysis(Analysis const & other);
		Analysis & operator = (const Analysis & other);
		
		void deleteKeys();
		void recreateKeys();
		const char ** keys;
		std::map<std::string, wchar_t *> attributes;
};

} }

#endif
